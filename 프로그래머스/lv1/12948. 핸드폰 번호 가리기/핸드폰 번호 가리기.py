def solution(phone_number):
    return ''.join(['*' for _ in range(len(phone_number)-4)] + list(phone_number[-4:]))