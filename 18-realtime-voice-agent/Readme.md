## Setup
- Create an account on [cerebrium](https://www.cerebrium.ai/)
    - In your Cerebrium dashboard, you can add your HuggingFace token as a secret by navigating to “Secrets” in the sidebar.
- Create an account on [Daily](https://dashboard.daily.co/u/signup)
    - You can then go to the “developers” tab to fetch your API key - add this to your Cerebrium Secrets.
- git clone git@github.com:facundo-zalazar/examples.git
    - go to /examples/18-realtime-voice-agent
    - pip install --upgrade cerebrium
    - cerebrium login
    - cerebrium deploy
- On cerebrium dashboard, check the Apps section, go to your deployed application, in the overview tab you will see a python example code. Copy the url and header from there and replace it on the run.py file accordingly
    - line 6 for headers
    - line 11 for URL/create_room
    - line 23 for URL/start_bot

- git clone https://github.com/pipecat-ai/web-client-ui
    - Setup your .env.example file as follows:
        - VITE_APP_TITLE=Simple Chatbot
        - VITE_SERVER_URL=... #optional: if serving frontend externally from backend, or requesting agent from API
        - VITE_MANUAL_ROOM_ENTRY=... #optional: require user to specify a room URL to join 
        - VITE_OPEN_MIC= # Can the user speak freely, or do they need to wait their turn? 
        - VITE_USER_VIDEO= #Does the app require the user's webcam?
        - VITE_SHOW_SPLASH=1 # Show a splash page with marketing info
        - VITE_SHOW_CONFIG= # Show demo config options first
        - VITE_SERVER_URL=https://api.cortex.cerebrium.ai/v4/p-76b6765f/18-realtime-agent (YOUR DEPLOYED APP LINK IS HERE)
        - VITE_SERVER_AUTH=eyJhbGciO... (TAKE THIS FROM THE API KEYS SECTION ON CEREBRIUM SIDEBAR)
    - mv env.example .env.development.local
    - yarn 
    - yarn run build
    - yarn dev

## Develop/test:
    - Make changes on the code
    - run
        - on a terminal tab with examples/18-realtime-voice-agent/ folder open
            - cerebrium deploy
            - python3 run.py
            - Take notes of the URL that is created. Check logs on App > logs on cerebrium dashboard
        - on a terminal tab with examples/web-client-ui folder open
            - yarn dev
            - Go to http://localhost:5173/
            - Enter to a meeting room with the URL that you noted above