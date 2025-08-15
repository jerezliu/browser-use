import asyncio
import os
import sys

from browser_use.llm.openai.chat import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()


from browser_use import Agent
from browser_use.browser.profile import BrowserProfile

# Initialize the model
llm = ChatOpenAI(
	model='gpt-5-mini',
)

# Create a browser profile with the sandbox disabled for Docker
browser_profile = BrowserProfile(chromium_sandbox=False)

task = 'Go to google.com/travel/flights and find the cheapest flight from New York to Paris on 2025-07-15'
agent = Agent(task=task, llm=llm, browser_profile=browser_profile)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
