Task 1: API Automation Using Requests
Use the public API https://jsonplaceholder.typicode.com/posts

Write a Python script to:

Fetch all posts.

Validate that the response status code is 200.

Verify each post contains the keys: userId, id, title, body.

Save the first 5 posts into a local JSON file.

**Answer in fetch_and_save_posts.py**

Task 2 : Pytest Test Suite

Create a Pytest test suite for the API in Section A.

Cover:

Response time < 2 seconds

Schema validation (use pydantic or jsonschema)

Parameterized test: Validate multiple endpoints (e.g., /posts, /comments, /users).

Ensure the suite can be executed with pytest -v.

**Answer in task2_api_suite.py**

Task 3: Postman Automation

Create a Postman collection with the following:

GET /posts – validate status = 200.

POST /posts – create a new post and verify the response contains the same title/body.

DELETE /posts/{id} – verify response status 200 or 204.

Add test scripts in Postman to validate responses.

Export and submit the Postman collection JSON file.

**Answer in Assessment.postman_collection.json**

Task 4 : Selenium with Pytest or Pytest Playwright automation

      https://rahulshettyacademy.com/AutomationPractice/
     
Select any elements and write Playwright code.**

**Answer in task4.py**

Task 5: Strategy & Leadership (Short Answers)

You are leading a team of 4 QA engineers. The sprint velocity is dropping due to flaky automation tests. How will you handle this situation?

During production release, you find 2 critical bugs reported by the client that were missed in QA. What’s your approach to fix gaps in process and testing?

**Answer in Task5.txt**
