from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from api_handler import api_handler
import uvicorn
import json


app = FastAPI()
origins = [
    "http://localhost:3000",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



    
@app.get('/')
def root():
    return {'hi': 'bye'}
    # return app.send_static_file('index.tsx')

@app.get('/regions')
async def get_regions():
    return {'regions': ['West','Southeast', 'Southwest', 'Northeast', 'Midwest']}

@app.get('/genders')
async def get_genders():
    return {'genders': ['Male', 'Female']}

@app.get('/ethnicities')
async def get_ethnicities():
    return {'ethnicities': 
        ['Asian', 'Black or African American', 
        'Native Hawaiian or Other Pacific Islanders', 
        'Hispanic or Latino', 'Two or More Races', 
        'American Indian or Alaska Native', 
        'White']}


@app.post('/{region}/{gender}/{race}') #respond to get request at this URL
async def run_tasks(file_enrollment: UploadFile = File(...), file_grad: UploadFile = File(...), region=None, gender=None, race=None):
    file_enrollment_bytes = await file_enrollment.read()
    file_grad_bytes = await file_grad.read()
    return api_handler() \
        .return_all_metrics(file_enrollment_bytes, file_grad_bytes, region, gender, race)


@app.get('/enroll-over-time/{region}/{gender}/{race}') #respond to get request at this URL
async def get_over_time_data_enroll(region=None, gender=None, race=None):
    return api_handler().get_data_over_time(region, gender, race, "Enrollment")

@app.get('/grad-over-time/{region}/{gender}/{race}') #respond to get request at this URL
async def get_over_time_data_grad(region=None, gender=None, race=None):
    return api_handler().get_data_over_time(region, gender, race, "Graduation")

@app.post('/enroll-current/{region}/{gender}/{race}') #respond to get request at this URL
async def get_current_data_enroll(file_enrollment: UploadFile = File(...),region=None, gender=None, race=None):
    file_enrollment_bytes = await file_enrollment.read()
    return api_handler().get_current_data(file_enrollment_bytes, region, gender, race, 'Enrollment')



@app.post('/grad-current/{region}/{gender}/{race}') #respond to get request at this URL
async def get_current_data_grad(file_grad: UploadFile = File(...), region=None, gender=None, race=None):
    file_grad_bytes = await file_grad.read()
    return api_handler().get_current_data(file_grad_bytes, region, gender, race, 'Graduation')

