"""
Задача:
- Реализовать возможность перевода денег между счетами
- Гарантировано публиковать сообщение в шину о произведенной транзакции
"""

from datetime import datetime

from fastapi import FastAPI, Body
from pydantic import BaseModel

import fake_db
from broker import get_message_broker


### DATABASE MODELS ###
class Account(fake_db.Model):
    id = fake_db.IntegerField(primary_key=True, autoincrement=True)
    balance = fake_db.IntegerField()

class Transaction(fake_db.Model):
    id = fake_db.IntegerField(primary_key=True, autoincrement=True)
    sender_id = fake_db.ForeignKey(Account)
    recipient_id = fake_db.ForeignKey(Account)
    amount = fake_db.FloatField()
    created = fake_db.DateTimeField(default=datetime.now)


### REQUEST ###
class PaymentRequest(BaseModel):
    sender_id: int
    recipient_id: int
    amount: float


### APPLICATION ###
app = FastAPI()

# async with fake_db.atomic():

@app.post("/payments")
async def makePayment(request: PaymentRequest = Body(...)):
    Sender = await Account.get(id=request.sender_id)
    Recipient = await Account.get(id=request.recipient_id)
    Sender.balance = Sender.balance - request.amount
    Recipient.balance = Recipient.balance + request.amount

    broker = get_message_broker()
    async with fake_db.atomic() as a:
        transaction = await Transaction.insert(
            sender_id=request.sender_id,
            recipient_id=request.recipient_id,
            amount=request.amount,
        )
        await asyncio.gather(*[Sender.save(), Recipient.save()])

    broker.publish(
        {
            "event_type": "transaction.created",
            "event_data": {
                "id": transaction.id,
                "sender_id": request.sender_id,
                "recipient_id": request.recipient_id,
                "amount": request.amount,
                "created": transaction.created,
            }
        }
    )
