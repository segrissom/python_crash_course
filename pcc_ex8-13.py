# This is from Python Crash Course from Chapter 8, exercise 13


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


build_profile('Sarah', 'G',  hair_color='Blonde', pets='Dog', sex='woman')
