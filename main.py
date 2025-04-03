import logging
from supabase import create_client
import os
from dotenv import load_dotenv


def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.INFO)

    load_dotenv()
    client = create_client(
        os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    )
    query = client.table("documents").select("*")

    id1 = "d7bcfc0a-3651-4bc2-94de-7ad8b840d222"
    id2 = "ca88aca3-6e30-4aaf-a837-11655bf6f187"

    query.in_("id", [id1]).execute()
    query.in_("id", [id2]).execute()


if __name__ == "__main__":
    main()
