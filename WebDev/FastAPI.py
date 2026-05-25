# imp components of fastapi
"""FastAPI consists of path operations, Pydantic models for validation, dependency injection, middleware, 
exception handling, background tasks, security utilities, and automatic API documentation powered by OpenAPI."""

#How do you stop scheduled background tasks after certain days?
"""In FastAPI with APScheduler, I use end_date while scheduling the job so it automatically 
stops after a defined time.
In Django with Celery, I prefer controlling it via database flags or disabling the periodic task 
using django-celery-beat for better production safety and multi-worker support."""

# serialization at fastapi
"""In FastAPI, serialization is handled by Pydantic models using the model_dump() method 
(previously dict() in Pydantic v1). FastAPI automatically converts the response model into JSON."""

# how to implement pagination in django/fastapi?
"""In Django, pagination can be implemented using Django Paginator or DRF built-in pagination classes 
like PageNumberPagination, LimitOffsetPagination, or CursorPagination. In FastAPI, we manually implement 
limit-offset logic or use fastapi-pagination for production-ready APIs."""

# "How do you avoid N+1 queries in FastAPI?"
"""In FastAPI, when using SQLAlchemy ORM, the N+1 query problem can be avoided by eager loading 
relationships using options like joinedload(), selectinload(), or subqueryload(). These allow related 
data to be fetched efficiently in fewer queries, similar to Django's select_related and prefetch_related."""

# What is dependency injection ?
"""Dependency Injection is a design pattern in which dependencies required by a class or function are provided 
from outside rather than being created internally. It helps in loose coupling, better testability, maintainability, 
and cleaner architecture. DI in FastAPI allows reusable components like DB sessions, authentication logic, 
and services to be automatically provided to route handlers using Depends(), improving modularity, maintainability, 
and testability."""