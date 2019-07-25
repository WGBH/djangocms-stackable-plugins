
def format_hostedvideo_duration(duration):
    hours = minutes = seconds = 0
    parts = str(duration).split(':')

    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(float(parts[2]))
    elif len(parts) == 2:
        minutes = int(parts[0])
        seconds = int(float(parts[1]))
    elif len(parts) == 1:
        seconds = int(float(parts[0]))
        
    if hours > 0:
        return "%d HRS %02d MIN %02d SEC" % (hours, minutes, seconds)
    else:
        if minutes > 0:
            return "%d MIN %02d SEC" % (minutes, seconds)
        else:
            if seconds > 0:
                return "%d SEC" % seconds
    return None