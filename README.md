# Students Registration API

This is a simple API project that should provide a CRUD for archiving students registration info.

## Usage

In order to run the application:

To build image
```commandline
docker build -t student-registration-image:latest .
```

To run the container
```commandline
docker compose up -d
```

## Data Base Structure

<div style="display: inline-block"></br>
    <img alt="DB Diagram" align="center" src='https://drive.google.com/uc?export=view&id=1QjwkEH85OtjmY6fNm8cJR-KKsrtgqoda'>
</div></br>

## Endpoints

There are 2(two) endpoints here:

```commandline
{
    "student": "http://127.0.0.1:8000/v1/api/student/",
    "registration": "http://127.0.0.1:8000/v1/api/registration/"
}
```
Those endpoints provides unique payloads, the first one provides basic information about the student, creating this
one allow us to create the registration. The payload from it has the following structure:

```commandline
{
    "id": "f5869422-5a0e-444c-8e9d-99f00ffd63d9",
    "name": "Some student`s name",
    "id_doc": "99999999999",
    "created_at": "2022-12-13T18:28:47.371501-03:00"
}
```

The second one will provide information about the student registration. The payload structure to this one is:

```commandline
{
    "id": 1,
    "email": "some_student@domain.com",
    "phone": "Some student phone number",
    "gender": "male",
    "degree": "other",
    "contact_name": "Some student`s second or responsible contact",
    "contact_number": "Responsible contact number",
    "relationship": "mother",
    "student": "5456ce9d-8a91-430d-8a01-db0ed614077e"
}
```

To successfully create this registration profile we must have the "student" ID generated by the first one.

## HTTP Requests Collection

The links bellow allow you to download each collection`s .json file.

[Student Registration Collection](https://drive.google.com/uc?export=view&id=1PFiODE3eKAsQ9-HgMN7RunJAHqa1Dw9s)</br>

## License

[MIT](https://choosealicense.com/licenses/mit/)
