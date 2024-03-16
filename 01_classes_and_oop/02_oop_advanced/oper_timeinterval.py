
class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.seconds = hours * 3600 + minutes * 60 + seconds
    
    def __str__(self) -> str:
        hours, minutes, seconds = self._parse(self.seconds)
        return f"{hours}:{minutes}:{seconds}"
    
    def _check_instance(self, other):
        assert isinstance(other, TimeInterval), "The argument must be an instance of TimeInterval class"
        
    def _parse(self, all_seconds):
        hours = all_seconds // 3600
        minutes = (all_seconds - hours * 3600) // 60
        seconds = all_seconds - hours * 3600 - minutes * 60
        return hours, minutes, seconds
    
    def __neg__(self):
        hours, minutes, seconds = self._parse(self.seconds)
        return TimeInterval(-hours, -minutes, -seconds)
    
    def __add__(self, other):
        if isinstance(other, int):
            other = TimeInterval(0, 0, other)
        self._check_instance(other)
        hours, minutes, seconds = self._parse(self.seconds + other.seconds)
        return TimeInterval(hours, minutes, seconds)
        
    def __sub__(self, other):
        return self.__add__(-other)
    
    def __mul__(self, other):
        assert type(other) == int, "The argument must be an integer"
        hours, minutes, seconds = self._parse(self.seconds * other)
        return TimeInterval(hours, minutes, seconds)
    

t1 = TimeInterval(21,58,50)
t2 = TimeInterval(1,45,22)

print(f"t1 = {t1}")
print(f"t2 = {t2}")
print(f"t1 + t2 = {t1 + t2}")
print(f"t1 - t2 = {t1 - t2}")
print(f"t1 * 2 = {t1 * 2}")

assert str(t1 + t2) == "23:44:12"
assert str(t1 - t2) == "20:13:28"
assert str(t1 * 2) == "43:57:40"

print("PART 1: Everything works as expected!")

t3 = TimeInterval(21,58,50)

print(f"t3 + 62 = {t3 + 62}")
print(f"t3 - 62 = {t3 - 62}")

assert str(t3 + 62) == "21:59:52"
assert str(t3 - 62) == "21:57:48"

print("PART 2: Everything works as expected!")