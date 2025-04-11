

from tools.email_utils import fetch_unread_emails, send_email
from workflow.email_response_flow import email_response_flow

def run():
    print("📬 Checking for new emails...")
    emails = fetch_unread_emails()

    if not emails:
        print("📭 No new emails found.")
        return

    print(f"📥 {len(emails)} new email(s) found.\n")

    for i, email in enumerate(emails):
        print(f"\n📨 Processing Email #{i+1}: {email['subject']}")
        result = email_response_flow(email)

        print(f"🧠 Classification: {result['classification']}")
        print(f"💬 AI Reply:\n{result['reply']}\n")

        if result.get("escalated"):
            print("⚠️ This email was escalated to a human. No auto-reply sent.\n")
            continue

       
        should_send = input("✅ Send this reply? (y/n): ").strip().lower()
        if should_send == 'y':
            send_email(result["from"], f"Re: {result['subject']}", result["reply"])
            print("📤 Email sent successfully.\n")
        else:
            print("⏭️ Skipped sending this email.\n")

if __name__ == "__main__":
    run()
