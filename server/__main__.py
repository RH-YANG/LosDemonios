if __name__ == '__main__':
    import uvicorn
    from dotenv import load_dotenv
    import os

    load_dotenv()

    port = int(os.getenv("API_PORT"))
    host = os.getenv("SERVER_ADDR")

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True, workers=3)