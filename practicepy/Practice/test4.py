from datetime import datetime

def validate_utc_timestamp(timestamp):
    import pdb;pdb.set_trace()
    try:
        # Attempt to parse the timestamp string
        dt = datetime.fromisoformat(timestamp)
        import pdb;pdb.set_trace()

        # Ensure that the timezone is UTC
        if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) != datetime.utcnow().tzinfo.utcoffset(dt):
            return False
        return True
    except Exception as e:
        # If parsing fails, return False
        print(e)

        return False

validate_utc_timestamp("78--invalid")


# Test cases
# timestamps = [
#     "78--invalid",
#     "2024-04-27T15:30:00Z",         # Valid UTC timestamp
#     "2024-04-27T15:30:00+00:00",    # Valid UTC timestamp with explicit timezone
#     "2024-04-27T15:30:00+02:00",    # Not UTC, has offset
#     "2024-04-27T15:30:00",           # No timezone information
#     "2024-04-27 15:30:00",           # Invalid format
# ]
#
# for timestamp in timestamps:
#     if validate_utc_timestamp(timestamp):
#         print(f"{timestamp} is a valid UTC timestamp.")
#     else:
#         print(f"{timestamp} is not a valid UTC timestamp.")
