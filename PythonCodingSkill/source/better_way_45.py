# 협정 세계시(UTC, Coordinated Universal Time)는 시간대에 의존하지 않는 표준 시간 표현이다.
# UTC는 유닉스 기원 이후로 지나간 초로 시간을 표현하는 컴퓨터에서 잘 작동한다.

# time 모듈
from time import localtime, strftime

now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)

print(time_str)

from time import mktime, strptime

time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

# 샌프란시스코에서 뉴욕으로 이동하는 비행기를 타고 뉴욕에 도착한 후 샌프란시스코의 시간을 알고 싶다고 하자.
# time, localtime, strptime 함수의 반환 값을 직접 조작해서 시간대를 변환하는 건 좋지 못한 생각이다.
# 시간대는 지역 규칙에 따라 모든 시간을 변경한다.
# parse_format = '%Y-%m-%d %H:%M:%S %Z'
# depart_sfo = '2014-05-01 15:45:16 PDT'
# time_tuple = strptime(depart_sfo, parse_format)
# time_str = strftime(time_format, time_tuple)
# print(time_str)

# 플랫폼에 의존적인 time 모듈의 특성 때문에 time 모듈의 기능을 신뢰하기 어렵다.
# 다른 형태의 변환에는 datetime 모듈을 사용해야 한다.

print('---------------------------')
# datetime 모듈
from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)

time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)

# datetime 모듈은 time 모듈과 달리 한 지역 시간을 다른 지역 시간으로 신뢰성 있게 변경한다.
# 하지만 tzinfo 클래스와 관련 메서드를 이용한 시간대 변환 기능만 제공한다.
# 빠진 부분은 UTC 이외의 시간대 정의다. pytz 모듈로 해결

# pytz를 효율적으로 사용하기 위해서는 항상 지역 시간을 utc로 먼저 변경해야 한다.
# 그리고 나서 UTC 값에 필요한 datetime 연산(오프셋 지정 등)을 수행한다.
import pytz

arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)

eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)

pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)

seoul = pytz.timezone('Asia/Seoul')
seoul_dt = seoul.normalize(utc_dt.astimezone(seoul))
print(seoul_dt)
