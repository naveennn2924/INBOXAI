# AI Email Auto-Responder **INBOXAI** 📧🤖

Welcome to the **AI Email Auto-Responder** project! This is an innovative email management system powered by **multi-agent AI** technology. The system automates email classification and response generation, leveraging **GPT-4o mini** to provide personalized, context-aware email replies. It's designed to be fully **local**, offering enhanced privacy and control over your email data.

## Key Features 🚀

- **Multi-Agent System**: A collaborative set of **autonomous agents** works in tandem to classify, generate, and send email responses, ensuring a seamless experience.
- **AI-Powered Replies**: Using the **GPT-4o mini model**, the system automatically generates personalized, human-like responses for various email types.
- **Escalation Workflow**: Complex emails are escalated to the appropriate agent for more detailed handling.
- **Data Privacy**: Everything runs **locally**, ensuring that all your email data remains private and secure—no external cloud services required.
- **Open-Source**: Developed using **open-source technologies**, this project invites community collaboration and innovation.

## How It Works 🔧

1. **Fetch Unread Emails**: The system integrates with your email provider and fetches **unread emails** from your inbox.
2. **Email Classification**: Incoming emails are classified into different categories such as **inquiries**, **notifications**, **meeting requests**, and more.
3. **AI Response Generation**: The system uses **GPT-4o mini** to generate context-aware email replies.
4. **Escalation**: Emails that require more complex or personalized responses are escalated to the relevant agents or human reviewers.
5. **Replying to Emails**: AI-generated replies are sent automatically to the original sender.

## Technologies Used 🛠️

- **Python** for back-end development
- **Streamlit** for the front-end UI
- **IMAP** and **SMTP** for email handling
- **GPT-4o mini model** for AI-powered text generation
- **Open-source libraries**: **dotenv**, **smtplib**, **email**, **email.mime**

## Installation 💻

To run the **AI Email Auto-Responder** on your machine, follow these simple steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-email-auto-responder.git
   
   cd ai-email-auto-responder

2. Install the required Python packages:
   
   pip install -r requirements.txt

3. Set up your .env file: Create a .env file in the project root and add the following details:
   
   EMAIL_ADDRESS=your-email@example.com
   
   EMAIL_PASSWORD=your-password
   
   IMAP_SERVER=imap.example.com
   
   SMTP_SERVER=smtp.example.com
   
   SMTP_PORT=587

4. Run the Streamlit app:
  
   streamlit run app.py



##  Usage 📈

Once the app is running, you can interact with the Streamlit UI to manage your emails:

**Fetch New Emails:** Click "Fetch New Emails" to retrieve unread emails.

**View & Respond:** Review AI-generated email responses, make edits, and send replies with a click of a button.

**Customization:** You can adjust settings (e.g., temperature, max tokens) to fine-tune the AI's responses in the code.

## Contributing 🤝

We welcome contributions! Here are some ways you can help improve this project:

**Enhance Features:** Add new functionalities or improve existing ones.

**Optimize AI Responses:** Tweak AI settings or improve the response generation logic.

**Improve Documentation:** Help make the project more accessible by enhancing the docs or UI.

**Report Bugs:** Let us know if you encounter any issues, and we’ll fix them promptly.

## License 📄

This project is licensed under the MIT License – see the LICENSE file for more details.


