from django.db import models


# 블랙보드 Stream에서 읽어온 값들 저장할 모델 - 과제에 초점이 맞춰져 있음
class Data(models.Model):
    sort = models.CharField(max_length=20)  # 종류(공지사항, 과제, ..)
    context_ellipsis = models.TextField()  # 과목
    name = models.TextField()  # 제목
    content = models.TextField()  # 내용
    time = models.DateTimeField(null=True)
    # time = models.DateTimeField(input_formats=["%Y년 %m월 %d일 %A %H:%M"])  # 마감기한
    # year = models.CharField(max_length=10, default='년')
    # month = models.CharField(max_length=10, default='월')
    # day = models.CharField(max_length=10, default='일')
    # date = models.CharField(max_length=10, default='요일')
    # hour = models.CharField(max_length=10, default='시')
    # minute = models.CharField(max_length=10, default='분')

    def __str__(self):
        return self.context_ellipsis + " " + self.sort


# 수업 시간표 저장할 모델
class TimeTable(models.Model):
    prof = models.TextField()  # 교수님
    subject = models.TextField()  # 과목명
    date = models.CharField(max_length=10, default='요일')
    start_h = models.IntegerField()
    end_h = models.IntegerField()

    def __str__(self):
        return self.subject + " - " + self.prof
