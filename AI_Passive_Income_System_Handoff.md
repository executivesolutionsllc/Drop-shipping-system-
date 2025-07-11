
# AI-Powered Automated Passive Income System - Full Handoff Document

---

## 1. Overview

Build a **scalable, multi-instance AI-powered passive income platform** that:

- Runs **3+ parallel content pipelines** in niches like Motivational/Law of Attraction, Mindfulness/Productivity, and Wealth Mindset.
- Fully automates **keyword research, script & blog generation, voiceover, video production, publishing, analytics collection, and reporting.**
- Monetizes content via **YouTube AdSense, blog ads, CPA offers, Amazon Associates, Digistore24, and digital products.**
- Provides a **unified, secure, mobile-friendly dashboard** for monitoring, control, scheduling, and reporting.
- Supports **multi-platform publishing:** YouTube, WordPress, TikTok, Instagram.
- Enables **API-based orchestration** via Make.com or n8n with robust error handling and logging.
- Incorporates **security best practices**: encrypted API key storage, role-based access, and compliance with FTC and platform terms.

---

## 2. System Architecture & Workflow

### High-level Pipeline per system

\`\`\`mermaid
flowchart LR
  subgraph Dashboard
    D[Glide/Pory Web & Mobile App]
  end
  D -->|Trigger Pipeline| Orchestration[(Make.com / n8n Workflow)]
  Orchestration --> KR[Keyword Research (Ahrefs/SEMrush API)]
  KR --> GC[Generate Content (GPT-4o API)]
  GC --> VO[Generate Voiceover (ElevenLabs API)]
  VO --> VD[Video Production (Pictory.ai / Synthesia API)]
  VD --> PU[Publish Content]
  PU -->|Long-Form| YT[YouTube via Data API]
  PU -->|Articles| WP[WordPress REST API]
  PU -->|Short-Form| TT[ TikTok/IG APIs]
  YT & WP & TT --> AN[Analytics Collection (Google Analytics & YouTube Analytics)]
  AN --> RP[Reporting & Feedback Loop (Google Sheets)]
  RP --> KR
\`\`\`

### Daily Scheduled Runs

- Run pipeline 5x daily (e.g., 2 AM, 7 AM, 12 PM, 5 PM, 10 PM) per system.
- Each run:
  - Fetch 20-30 relevant keywords (via Ahrefs/SEMrush API)
  - Generate scripts, blog drafts, captions (GPT-4o)
  - Produce voiceover files (ElevenLabs)
  - Assemble video with captions, thumbnails (Pictory.ai or Synthesia)
  - Upload videos & posts
  - Distribute shorts/teasers on TikTok/IG
  - Pull analytics and update dashboard
  - Send detailed progress & revenue reports via email/Slack/SMS

---

## 3. Core Accounts and APIs Setup

| Platform           | Purpose                      | Notes / Credentials Setup                          |
|--------------------|------------------------------|---------------------------------------------------|
| **Ahrefs/SEMrush** | Keyword research API          | API key, limits, query configuration               |
| **OpenAI GPT-4o**  | Content generation (scripts, blog, captions) | API key, prompt templates                           |
| **ElevenLabs**     | AI voiceover                  | Voice profile setup, API keys                       |
| **Pictory.ai / Synthesia** | Video production           | API access, templates                                |
| **YouTube Data API** | Upload & manage videos       | OAuth2 with upload scope, channel configuration     |
| **WordPress REST API** | Publish articles             | Auth token (OAuth/Basic), post formatting           |
| **TikTok & Instagram APIs** | Distribute shorts/teasers | Developer accounts, access tokens                    |
| **Google Analytics & YouTube Analytics** | Collect performance data | OAuth2, API scopes                                    |
| **Affiliate Networks** | Monetization (CPAgrip, Amazon Associates, Digistore24) | Account IDs, affiliate links, tracking setup         |
| **Gmail/Slack/SMS Gateways** | Notifications & reports   | SMTP credentials, Slack webhook URLs, SMS provider API |

---

## 4. Infrastructure & Automation Platform

### Orchestration platform (Choose one)

- **Make.com**: Visual scenario builder, triggers, data handling
- **n8n**: Self-hosted or cloud, node-based workflows, full JavaScript customization

### Infrastructure components

- **Google Sheets** for topic queue, analytics tracking, content metadata
- **Glide or Pory** for dashboard front-end (mobile & desktop)
- **Secure storage** of API keys (Make.com vault, n8n credential manager, or AWS/GCP secrets)
- **Notification triggers** for success/failure (Slack/Gmail/SMS)

---

## 5. Pipeline Workflow Steps (Detailed)

| Step                     | Description                                                  | Tools & APIs                             |
|--------------------------|--------------------------------------------------------------|----------------------------------------|
| **Trigger Pipeline**       | Manual or scheduled run initiates full pipeline             | Glide/Pory → Make.com or n8n            |
| **Keyword Research**       | Query Ahrefs/SEMrush API for trending, low-competition keywords | Ahrefs/SEMrush API                      |
| **Content Generation**     | Generate scripts, blog drafts, social captions with GPT-4o   | OpenAI GPT-4o API, prompt templates    |
| **Voiceover Production**   | Create natural-sounding narration using ElevenLabs           | ElevenLabs API                         |
| **Video Assembly**         | Auto-assemble videos using voiceover and captions            | Pictory.ai or Synthesia API             |
| **Publishing**             | Upload video to YouTube; post blog to WordPress; push shorts to TikTok/IG | YouTube Data API, WordPress REST API, TikTok/IG APIs |
| **Analytics Collection**   | Retrieve analytics from Google Analytics & YouTube Analytics | GA API, YouTube Analytics API           |
| **Reporting & Feedback**   | Update Google Sheets with metrics and send summary reports   | Google Sheets API, Gmail/Slack/SMS     |
| **Monetization Tracking**  | Track affiliate clicks, ad revenue, product sales            | CPAgrip, Amazon Associates, Digistore24 dashboards/APIs |

---

## 6. Security & Compliance

- Encrypt all API keys and tokens in secure vaults
- Apply least-privilege access principles to API scopes
- Rotate API keys quarterly
- Implement monitoring & alerting on workflow failures or abnormal activity
- Include FTC-compliant affiliate disclosures in all content
- Abide by YouTube, WordPress, TikTok, Instagram terms of service

---

## 7. Scaling & Maintenance

- Add new niche vertical pipelines (e.g., Spiritual Healing, Wealth Mindset)
- Refresh voiceover personas quarterly for engagement
- Audit content monthly to recycle or update low-performing posts
- Integrate additional affiliate programs (ClickBank, JVZoo)
- Maintain a centralized prompt library and SOP docs for content generation

---

## 8. Deliverables for Development Team or AI Assistant

1. Fully configured Make.com or n8n workflow orchestrating all pipeline steps for each niche system.
2. Secure API key storage and retrieval system.
3. Google Sheets integration for keyword queue and analytics dashboard.
4. Glide or Pory app as unified multi-system dashboard with:
   - Run / schedule toggle buttons
   - Real-time status and analytics view
   - Regenerate content buttons
5. Automated publishing scripts using YouTube, WordPress, TikTok, and Instagram APIs.
6. Affiliate link injection logic with randomized A/B testing support.
7. Email/Slack/SMS report generation and dispatch modules.
8. Logging and error recovery logic with alerts.

---

## 9. Example Code Snippet (YouTube Upload via Python)

\`\`\`python
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

def upload_video(file_path, title, description, tags, category_id=22):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'public'
        }
    }
    
    media_file = MediaFileUpload(file_path)
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    )
    response = request.execute()
    return response['id']
\`\`\`

---

# AI Development Prompt (For GPT-4 / Codex / AI Coding Assistant)

---

**Prompt Title:** Develop Full AI-Powered Automated Passive Income Content Pipeline System

---

**Prompt:**

I want you to build a **fully automated, scalable AI-powered passive income platform** consisting of **three parallel niche pipelines** (Motivational/Law of Attraction, Mindfulness/Productivity, Wealth Mindset) that each run independently but are controlled via a single unified dashboard.

The system must:

- Automatically run 5 times per day, executing the full content pipeline end-to-end.
- Perform keyword research by querying the Ahrefs or SEMrush API.
- Generate persuasive scripts, blog drafts, and social captions via the OpenAI GPT-4o API using predefined prompt templates.
- Create studio-quality voiceovers with ElevenLabs API.
- Auto-produce videos using Pictory.ai or Synthesia APIs, assembling visuals, subtitles, and voiceover.
- Publish long-form videos to YouTube using YouTube Data API with proper OAuth authentication.
- Post corresponding blog articles to WordPress via REST API.
- Distribute short teaser videos or clips on TikTok and Instagram using their respective APIs.
- Collect detailed analytics from YouTube Analytics and Google Analytics APIs to track performance metrics (views, watch time, revenue, engagement).
- Store keyword queues, content metadata, and analytics in Google Sheets.
- Use Glide or Pory to create a mobile-friendly, secure dashboard that allows:
  - Manual trigger or scheduled runs of the pipeline
  - Viewing pipeline status in real time
  - Reviewing content performance analytics
  - Regenerating content on demand
- Support monetization through YouTube AdSense, CPAgrip affiliate offers, Amazon Associates, Digistore24 affiliate links, and digital product promotion.
- Implement secure API key storage, role-based dashboard access, and error notifications via Slack, Gmail, or SMS.
- Include affiliate link rotation and A/B testing capabilities in content generation.
- Provide logs and automated error recovery for workflow failures.

Deliver:

- Complete Make.com or n8n workflow JSON or scenario files for orchestration.
- Sample API integration code snippets (YouTube upload, WordPress post, TikTok upload).
- Prompt templates for OpenAI GPT-4o content generation with examples.
- Google Sheets setup templates for keyword queue and analytics tracking.
- Detailed README for deployment, maintenance, and scaling.

---

Please write modular, maintainable, and well-commented code, and provide instructions to configure all necessary API credentials and environment variables for secure operation.

---

If you'd like, I can also help generate specific code parts or setup steps upon request.
