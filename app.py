
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Page configuration
st.set_page_config(
    page_title="GramMate - AI Grammar Corrector",
    page_icon="✍️",
    layout="centered"
)

# 3. Application heading
st.title("✍️ GramMate")
st.subheader("AI-Powered Grammar Corrector")

st.write(
    "Improve your English writing using "
    "Artificial Intelligence and Large Language Models."
)

st.divider()

# 4. Check API key
if not API_KEY:
    st.error(
        "Gemini API key is missing. "
        "Please add GEMINI_API_KEY to your .env file."
    )
    st.stop()

# 5. Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# 6. User input
st.subheader("Enter Your Text")

user_text = st.text_area(
    "Your sentence or paragraph:",
    placeholder="Example: She don't likes coffee.",
    height=180
)

# 7. Select writing style
style = st.selectbox(
    "Choose correction style:",
    [
        "Basic Grammar Correction",
        "Professional English",
        "Simple English",
        "Academic English"
    ]
)

# 8. Explanation option
explain = st.checkbox(
    "Explain the grammatical mistakes"
)

# 9. Grammar correction function
def correct_grammar(text, style, explain):

    explanation_instruction = (
        "After correcting the text, explain the important "
        "grammatical mistakes and why they were corrected."
        if explain
        else "Return only the corrected text without explanations."
    )

    prompt = f"""
    You are an expert English grammar correction assistant.

    TASK:
    Correct the grammar, spelling and punctuation
    of the user's text.

    WRITING STYLE:
    {style}

    INSTRUCTIONS:
    1. Preserve the original meaning.
    2. Do not add unrelated information.
    3. Improve sentence structure where necessary.
    4. Maintain the selected writing style.
    5. Do not invent facts.

    OUTPUT:
    {explanation_instruction}

    USER TEXT:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# 10. Correct grammar button
if st.button("✨ Correct Grammar", type="primary"):

    if not user_text.strip():
        st.warning("Please enter some text first.")

    elif len(user_text) > 10000:
        st.warning(
            "Please enter text containing fewer than 10,000 characters."
        )

    else:
        with st.spinner("Gemini is correcting your text..."):

            try:
                result = correct_grammar(
                    user_text,
                    style,
                    explain
                )

                if not result:
                    st.error("The model returned an empty response.")

                else:
                    st.success("Grammar correction completed!")

                    # Display only corrected text
                    st.subheader("✅ Corrected Text")

                    st.text_area(
                        "Your corrected text:",
                        value=result,
                        height=220,
                        key="corrected_output"
                    )

                    st.code(result, language="text")

            except Exception as e:
                st.error(
                    "Unable to process your request. "
                    "Please check your API key, internet connection "
                    "and API quota."
                )

                st.caption(str(e))


# 11. Footer
st.divider()

st.caption(
    "GramMate | Powered by Google Gemini LLM"
)

st.caption(
    "Built using Python, Streamlit and Prompt Engineering."
)
