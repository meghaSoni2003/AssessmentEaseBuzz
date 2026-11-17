import json
import requests

BaseURL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_save_posts():
    try:
        # Fetch all posts.
        response = requests.get(BaseURL, timeout=10)
        print("1. Fetched all records")
        # Validate that the response status code is 200.
        assert (
            response.status_code == 200
        ), f"Expected status 200, got {response.status_code}"
        print("2. Validation passed: Status code is 200")

        posts = response.json()


        # Verify each post contains the keys: userId, id, title, body.
        required_keys = {"userId", "id", "title", "body"}

        for idx, post in enumerate(posts):
            missing_keys = required_keys - post.keys()
            assert not missing_keys, f"Post at index {idx} missing keys: {missing_keys}"

        print(
            f"3. Validation passed: All {len(posts)} posts contain the required keys ({required_keys})"
        )

        # Save first 5 posts into a local JSON file
        first_5_posts = posts[:5]
        with open("first_5_posts.json", "w", encoding="utf-8") as f:
            json.dump(first_5_posts, f, indent=4)
        print("4. File saved: First 5 posts saved to 'first_5_posts.json'")


    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except AssertionError as e:
        print(f"Validation Error: {e}")


if __name__ == "__main__":
    fetch_and_save_posts()