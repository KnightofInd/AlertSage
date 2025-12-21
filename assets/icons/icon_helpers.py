"""
AlertSage Icon Helpers
Utility functions for loading and displaying SVG icons in Streamlit
"""

from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components


def load_svg_icon(icon_name: str) -> str:
    """
    Load SVG icon and return as string.

    Args:
        icon_name: Name of the icon file (without .svg extension)

    Returns:
        SVG content as string, or empty string if file not found
    """
    # Get the directory where this file is located
    current_dir = Path(__file__).parent
    icon_path = current_dir / f"{icon_name}.svg"

    if icon_path.exists():
        return icon_path.read_text()
    return ""


def severity_badge(level: str, text: str = "", size: int = 24) -> str:
    """
    Display severity icon with optional text.

    Args:
        level: Severity level (critical, high, medium, low)
        text: Optional text to display next to icon
        size: Icon size in pixels (default: 24)

    Returns:
        HTML string with icon and optional text
    """
    icons = {
        "critical": "severity-critical",
        "high": "severity-high",
        "medium": "severity-medium",
        "low": "severity-low",
        "info": "severity-low",  # Use low/green for info
    }

    icon_name = icons.get(level.lower(), "severity-low")
    icon_svg = load_svg_icon(icon_name)

    # Return safe placeholder if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return f'<span>{text if text else ""}</span>'

    # Adjust SVG size
    if size != 24:
        icon_svg = icon_svg.replace('width="24"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="24"', f'height="{size}"')

    if text:
        return f"""
        <div style="display: inline-flex; align-items: center; gap: 8px;">
            {icon_svg}
            <span style="font-weight: 500;">{text}</span>
        </div>
        """
    return icon_svg


def feature_icon(icon_name: str, size: int = 32) -> str:
    """
    Display a feature icon (analysis, shield, threat-intel, mitre-attack).

    Args:
        icon_name: Icon name (analysis, shield, threat-intel, mitre-attack)
        size: Icon size in pixels (default: 32)

    Returns:
        HTML string with sized icon
    """
    icon_svg = load_svg_icon(f"{icon_name}-icon")

    # Return safe placeholder if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return "<span></span>"

    if size != 32:
        icon_svg = icon_svg.replace('width="32"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="32"', f'height="{size}"')

    return icon_svg


def status_badge(status: str = "analyzing") -> str:
    """
    Display an animated status badge.

    Args:
        status: Status type (analyzing, complete)

    Returns:
        HTML string with animated badge
    """
    badge_name = f"badge-{status}"
    icon_svg = load_svg_icon(badge_name)
    return icon_svg if icon_svg and icon_svg.strip() else "<span></span>"


def icon_button(icon_name: str, text: str, size: int = 20) -> str:
    """
    Create a button-like element with icon and text.

    Args:
        icon_name: Icon name (settings, export, upload, filter, user, bookmark)
        text: Button text
        size: Icon size in pixels (default: 20)

    Returns:
        HTML string for icon button
    """
    icon_svg = load_svg_icon(f"{icon_name}-icon")

    # Return text-only button if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return f'<span style="font-size: 14px; font-weight: 500;">{text}</span>'

    if size != 24:
        icon_svg = icon_svg.replace('width="24"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="24"', f'height="{size}"')

    return f"""
    <div style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; 
                border-radius: 8px; background: rgba(0, 102, 204, 0.05); 
                border: 1px solid rgba(0, 102, 204, 0.2); cursor: pointer;
                transition: all 0.2s ease;">
        {icon_svg}
        <span style="font-size: 14px; font-weight: 500;">{text}</span>
    </div>
    """


def logo_header(size: int = 60, show_tagline: bool = True) -> str:
    """
    Display AlertSage logo with optional tagline.
    Returns HTML string for use with st.markdown() or returns None if using components.

    For rendering in Streamlit, use logo_header_display() instead.

    Args:
        size: Logo size in pixels (default: 60)
        show_tagline: Whether to show tagline (default: True)

    Returns:
        HTML string with logo and optional tagline
    """
    import random

    logo_svg = load_svg_icon("alertsage-logo")

    # Fallback if logo doesn't load
    if not logo_svg or logo_svg.strip() == "":
        return '<div style="text-align: center;"><span style="font-size: 24px; font-weight: bold; color: #667eea;">AlertSage</span></div>'

    # Make gradient IDs unique to avoid conflicts when multiple logos on same page
    unique_id = f"{random.randint(10000, 99999)}"
    logo_svg = logo_svg.replace('id="logo-gradient"', f'id="logo-gradient-{unique_id}"')
    logo_svg = logo_svg.replace(
        "url(#logo-gradient)", f"url(#logo-gradient-{unique_id})"
    )
    logo_svg = logo_svg.replace('id="shield-glow"', f'id="shield-glow-{unique_id}"')
    logo_svg = logo_svg.replace("url(#shield-glow)", f"url(#shield-glow-{unique_id})")

    if size != 120:
        logo_svg = logo_svg.replace('width="120"', f'width="{size}"')
        logo_svg = logo_svg.replace('height="120"', f'height="{size}"')

    # Build HTML without extra whitespace
    if show_tagline:
        tagline_html = '<div style="margin-top: 8px; font-size: 14px; color: #8E8E93; font-weight: 500;">AI-Powered Security Intelligence Platform</div>'
        return f'<div style="display: flex; flex-direction: column; align-items: center;">{logo_svg}{tagline_html}</div>'
    else:
        return f'<div style="display: flex; flex-direction: column; align-items: center;">{logo_svg}</div>'


def logo_header_display(size: int = 60, show_tagline: bool = True, height: int = None):
    """
    Display AlertSage logo using Streamlit components (renders correctly).
    Use this function directly in Streamlit apps instead of logo_header().

    Args:
        size: Logo size in pixels (default: 60)
        show_tagline: Whether to show tagline (default: True)
        height: Component height in pixels (auto-calculated if None)
    """
    logo_html = logo_header(size=size, show_tagline=show_tagline)

    # Auto-calculate height based on size and tagline
    if height is None:
        height = size + 40 if show_tagline else size + 20

    components.html(logo_html, height=height)


def branded_metric_card(
    title: str, value: str, icon_name: str = None, color: str = "#667eea"
) -> str:
    """
    Create a branded metric card with optional icon.
    Returns HTML string for use with st.markdown(unsafe_allow_html=True).

    Args:
        title: Metric title
        value: Metric value to display
        icon_name: Optional icon name (e.g., 'shield', 'chart')
        color: Gradient color (default: brand purple)

    Returns:
        HTML string for metric card
    """
    icon_html = ""
    if icon_name:
        icon_svg = load_svg_icon(f"{icon_name}-icon")
        if icon_svg:
            # Resize to 32px for metric cards
            icon_svg = icon_svg.replace('width="24"', 'width="32"')
            icon_svg = icon_svg.replace('height="24"', 'height="32"')
            icon_svg = icon_svg.replace('width="32"', 'width="32"')
            icon_svg = icon_svg.replace('height="32"', 'height="32"')
            icon_html = f'<div style="margin-bottom: 8px;">{icon_svg}</div>'

    return f"""
    <div style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                padding: 1.5rem; border-radius: 12px; color: white;
                text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        {icon_html}
        <div style="font-size: 0.9rem; opacity: 0.9; margin-bottom: 4px;">{title}</div>
        <div style="font-size: 2rem; font-weight: bold;">{value}</div>
    </div>
    """


def section_header(text: str, icon_name: str = None, size: str = "large") -> str:
    """
    Create a branded section header with optional icon.
    Returns HTML string for use with st.markdown(unsafe_allow_html=True).

    Args:
        text: Header text
        icon_name: Optional icon name
        size: 'large', 'medium', or 'small'

    Returns:
        HTML string for section header
    """
    sizes = {"large": "2rem", "medium": "1.5rem", "small": "1.2rem"}
    font_size = sizes.get(size, "1.5rem")

    icon_html = ""
    if icon_name:
        icon_svg = load_svg_icon(f"{icon_name}-icon")
        if icon_svg:
            icon_size = "24" if size == "small" else "32" if size == "medium" else "40"
            icon_svg = icon_svg.replace('width="24"', f'width="{icon_size}"')
            icon_svg = icon_svg.replace('height="24"', f'height="{icon_size}"')
            icon_svg = icon_svg.replace('width="32"', f'width="{icon_size}"')
            icon_svg = icon_svg.replace('height="32"', f'height="{icon_size}"')
            icon_html = f'<span style="display: inline-block; vertical-align: middle; margin-right: 12px;">{icon_svg}</span>'

    return f"""
    <div style="font-size: {font_size}; font-weight: bold; 
                background: linear-gradient(90deg, #667eea, #764ba2);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                margin: 1rem 0; display: flex; align-items: center;">
        {icon_html}{text}
    </div>
    """


def inline_icon(icon_name: str, size: int = 16) -> str:
    """
    Display a small inline icon for use in text.

    Args:
        icon_name: Icon name
        size: Icon size in pixels (default: 16)

    Returns:
        HTML string for inline icon
    """
    # Determine the icon file based on name
    if icon_name in ["critical", "high", "medium", "low"]:
        svg_name = f"severity-{icon_name}"
        default_size = 24
    elif icon_name in ["settings", "export", "upload", "filter", "user", "bookmark"]:
        svg_name = f"{icon_name}-icon"
        default_size = 24
    elif icon_name in ["analysis", "shield", "threat-intel", "mitre-attack"]:
        svg_name = f"{icon_name}-icon"
        default_size = 32
    else:
        svg_name = icon_name
        default_size = 24

    icon_svg = load_svg_icon(svg_name)

    # Return safe placeholder if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return "<span></span>"

    if size != default_size:
        icon_svg = icon_svg.replace(f'width="{default_size}"', f'width="{size}"')
        icon_svg = icon_svg.replace(f'height="{default_size}"', f'height="{size}"')

    return f'<span style="display: inline-block; vertical-align: middle; margin: 0 4px;">{icon_svg}</span>'


# Quick access functions for common patterns
def critical_badge(text: str = "") -> str:
    """Display critical severity badge"""
    return severity_badge("critical", text)


def high_badge(text: str = "") -> str:
    """Display high severity badge"""
    return severity_badge("high", text)


def medium_badge(text: str = "") -> str:
    """Display medium severity badge"""
    return severity_badge("medium", text)


def low_badge(text: str = "") -> str:
    """Display low/success badge"""
    return severity_badge("low", text)


def incident_icon(incident_type: str, size: int = 24, with_text: bool = False) -> str:
    """
    Display incident type icon with optional text.

    Args:
        incident_type: Type of incident (phishing, malware, access_abuse, etc.)
        size: Icon size in pixels (default: 24)
        with_text: Whether to include incident type text (default: False)

    Returns:
        HTML string with incident icon
    """
    # Normalize incident type name
    type_map = {
        "phishing": "incident-phishing",
        "malware": "incident-malware",
        "access_abuse": "incident-access-abuse",
        "credential_compromise": "incident-credential-compromise",
        "data_exfiltration": "incident-data-exfiltration",
        "insider_threat": "incident-insider-threat",
        "policy_violation": "incident-policy-violation",
        "web_attack": "incident-web-attack",
        "suspicious_network_activity": "incident-suspicious-network",
        "benign_activity": "incident-benign",
        "uncertain": "incident-uncertain",
    }

    icon_name = type_map.get(incident_type, "incident-uncertain")
    icon_svg = load_svg_icon(icon_name)

    # Return safe placeholder if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return "<span></span>"

    if size != 24:
        icon_svg = icon_svg.replace('width="24"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="24"', f'height="{size}"')

    if with_text:
        display_name = incident_type.replace("_", " ").title()
        return f"""
        <div style="display: inline-flex; align-items: center; gap: 8px;">
            {icon_svg}
            <span style="font-weight: 500;">{display_name}</span>
        </div>
        """

    return icon_svg


def ui_icon(name: str, size: int = 24) -> str:
    """
    Display UI action/feature icon.

    Args:
        name: Icon name (confidence, classification, ai-engine, ioc, experimental, download, risk, construction)
        size: Icon size in pixels (default: 24)

    Returns:
        HTML string with icon
    """
    icon_svg = load_svg_icon(f"{name}-icon")

    # Return safe placeholder if icon doesn't load
    if not icon_svg or icon_svg.strip() == "":
        return "<span></span>"

    if size != 24:
        icon_svg = icon_svg.replace('width="24"', f'width="{size}"')
        icon_svg = icon_svg.replace('height="24"', f'height="{size}"')

    return icon_svg


# Example usage patterns
USAGE_EXAMPLES = """
# Usage Examples

## In Streamlit:

```python
import streamlit as st
from assets.icons.icon_helpers import (
    severity_badge, feature_icon, status_badge, 
    logo_header, icon_button, inline_icon
)

# Display severity with text
st.markdown(severity_badge("critical", "Critical Alert Detected"), unsafe_allow_html=True)

# Feature icon
st.markdown(feature_icon("shield", size=48), unsafe_allow_html=True)

# Animated status
st.markdown(status_badge("analyzing"), unsafe_allow_html=True)

# Logo in sidebar
st.sidebar.markdown(logo_header(size=80), unsafe_allow_html=True)

# Inline in text
st.markdown(f"Click {inline_icon('settings')} to configure", unsafe_allow_html=True)

# Icon button
st.markdown(icon_button("export", "Export Results"), unsafe_allow_html=True)
```

## Severity Levels in Metrics:

```python
# In metric displays
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(severity_badge("high", "High Risk Detected"), unsafe_allow_html=True)
```

## MITRE Techniques:

```python
st.markdown(f"{inline_icon('mitre-attack')} T1566.001 - Spearphishing", unsafe_allow_html=True)
```
"""
