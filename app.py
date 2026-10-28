import streamlit as st
from phishing_checker import check_url

st.set_page_config(
    page_title="Phishing URL Awareness Checker",
    page_icon="🛡️",
    layout="centered",
)

st.title("🛡️ Phishing URL Awareness Checker")
st.write(
    "Check a link for common phishing warning signs "
    "before deciding whether to trust it."
)

st.info(
    "Privacy notice: This tool examines URL text only. "
    "It does not open the website or send your URL to an external service."
)

st.subheader("Check a URL")

samples = {
    "Choose a sample URL": "",
    "Example URL": "https://www.example.com/login",
    "IP address with HTTP": "http://192.0.2.10/account",
    "@ symbol with HTTP": "http://example.com@sample.invalid/login",
    "Many hostname segments": "https://a.b.c.d.e.example.invalid/path",
    "Punycode-style hostname": "https://xn--example.invalid/",
}

sample_choice = st.selectbox(
    "Try a sample",
    list(samples.keys()),
)

url = st.text_input(
    "Enter the complete URL",
    value=samples[sample_choice],
    placeholder="https://www.example.com/login",
)

if st.button("Check URL", type="primary", use_container_width=True):
    try:
        warnings = check_url(url)

        st.subheader("Analysis Results")

        if warnings:
            st.warning(
                f"Review carefully: {len(warnings)} warning sign(s) found."
            )

            for warning in warnings:
                st.markdown(f"- {warning}")
        else:
            st.success("No listed warning signs found.")

        st.info(
            "Important: These checks cannot guarantee that a URL is safe. "
            "A phishing link may not show any of these warning signs."
        )

    except ValueError as error:
        st.error(str(error))

st.divider()

st.subheader("Six warning signs checked")

st.markdown(
    """
    1. An `@` symbol in the URL.
    2. A URL longer than 100 characters.
    3. An IP address used as the hostname.
    4. Five or more hostname segments.
    5. A punycode marker (`xn--`) in the hostname.
    6. The HTTP scheme instead of HTTPS.
    """
)

st.subheader("Stay safe online")

st.markdown(
    """
    - Never enter passwords or OTPs after following an unexpected link.
    - Check the domain carefully before signing in.
    - When in doubt, visit the organisation's official website directly.
    """
)

st.caption(
    "EWB educational project | Python and Streamlit | "
    "This tool is an awareness aid, not a complete security scanner."
)
