import uvicorn
from django.conf import settings

if __name__ == "__main__":
    uvicorn.run(
        "core.asgi:application",
        host="0.0.0.0",
        port=8000,
        lifespan="off",
        reload=True,
    )
