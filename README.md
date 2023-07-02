Steps in install the depencies
1. Install Flash version 2.3.2
2. Install Flask-Cors 4.0.0
3. Install Flask-MySQL 1.5.2

---

How to run the API
1. Open the project
2. Run ControllerAPI.py



---

Request and response documentation
1. Balance Inquiry - GET balance/:id 
- REQUEST : 
Params (Path Variable) - Key = id , Value = id 
- RESPONSE : 
[
    {
        "balance": 5000,
        "id": 1
    }
]

2. Cash in - POST /cashin
- REQUEST :
Body (raw) -
{
    "id": "1",
    "amount": "1"
}
- RESPONSE :
{
    "message": "Cash-in Successful!",
    "status": 200
}

3. Cash out - POST /cashout
- REQUEST :
Body (raw) -
{
    "id": "3",
    "amount": "200"
}
- RESPONSE :
{
    "message": "Cash-out Successful!",
    "status": 200
}
