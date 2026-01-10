# LMS API Test cURLs

Base URL: `http://localhost:8000`

## Setup
Set your access token as an environment variable (after login):
```bash
export TOKEN="your_access_token_here"
```

---

## 1. Users API (`/api/users/`)

### Register User (Student)
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "student1", "password": "password123", "email": "student1@example.com", "role": "student"}'
```

### Register User (Teacher)
```bash
curl -X POST http://localhost:8000/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "teacher1", "password": "password123", "email": "teacher1@example.com", "role": "teacher"}'
```

### Login (Get Access Token)
```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "teacher1", "password": "password123"}'
```
**Response:** Copy `access` and `refresh` tokens.

### Refresh Token
```bash
curl -X POST http://localhost:8000/api/users/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "YOUR_REFRESH_TOKEN"}'
```

---

## 2. Categories API (`/api/courses/categories/`)

### Create Category
```bash
curl -X POST http://localhost:8000/api/courses/categories/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Programming", "slug": "programming"}'
```

### List All Categories
```bash
curl -X GET http://localhost:8000/api/courses/categories/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 3. Courses API (`/api/courses/`)

### Create Course
```bash
curl -X POST http://localhost:8000/api/courses/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Django Fundamentals", "description": "Learn Django from scratch", "category": 1}'
```

### List All Courses
```bash
curl -X GET http://localhost:8000/api/courses/ \
  -H "Authorization: Bearer $TOKEN"
```

### Get Course Details
```bash
curl -X GET http://localhost:8000/api/courses/1/ \
  -H "Authorization: Bearer $TOKEN"
```

### Update Course (PUT)
```bash
curl -X PUT http://localhost:8000/api/courses/1/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Django Advanced", "description": "Advanced Django concepts", "category": 1}'
```

### Update Course (PATCH)
```bash
curl -X PATCH http://localhost:8000/api/courses/1/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Django Pro"}'
```

### Delete Course
```bash
curl -X DELETE http://localhost:8000/api/courses/1/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 4. Lessons API (`/api/lessons/`)

### Create Lesson
```bash
curl -X POST http://localhost:8000/api/lessons/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"course": 1, "title": "Introduction to Django", "video_url": "https://example.com/video1.mp4", "content": "Django is a web framework...", "order": 1}'
```

### List All Lessons
```bash
curl -X GET http://localhost:8000/api/lessons/ \
  -H "Authorization: Bearer $TOKEN"
```

### Get Lesson Details
```bash
curl -X GET http://localhost:8000/api/lessons/1/ \
  -H "Authorization: Bearer $TOKEN"
```

### Update Lesson (PUT)
```bash
curl -X PUT http://localhost:8000/api/lessons/1/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"course": 1, "title": "Django Setup", "video_url": "https://example.com/video2.mp4", "content": "Updated content", "order": 1}'
```

### Update Lesson (PATCH)
```bash
curl -X PATCH http://localhost:8000/api/lessons/1/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Django Installation"}'
```

### Delete Lesson
```bash
curl -X DELETE http://localhost:8000/api/lessons/1/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 5. Enrollments API (`/api/enrollments/`)

### Enroll in Course (as Student)
```bash
curl -X POST http://localhost:8000/api/enrollments/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"course": 1}'
```

### List My Enrollments
```bash
curl -X GET http://localhost:8000/api/enrollments/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## Testing Workflow

1. **Register a teacher** and **login** to get token
2. **Create a category**
3. **Create a course** (as teacher)
4. **Create lessons** for the course
5. **Register a student** and **login** with student credentials
6. **Enroll in the course** (as student)
7. **List enrollments** to verify
