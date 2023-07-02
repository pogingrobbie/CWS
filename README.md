import MYSQL
1. You can find the .mysql file on the repository "cws.sql"

import Postman Collection
1. You can find the collection on the repository "Bayad EXAM.postman_collection"


Steps in install the depencies
1. Install Flask version 2.3.2
2. Install Flask-Cors 4.0.0
3. Install Flask-MySQL 1.5.2
4. Install PyMySQL 1.1.0

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


TEST ID
1. 1
2. 2
3. 3