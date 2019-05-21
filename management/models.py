# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    userId = models.CharField(max_length=320) #이메일 최대 길이 RFC2822 정의 따름
    pw=  models.CharField(max_length=10)
    profileURL = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=10)
    sort = models.CharField(max_length=2)

    # 예시
    # m1 = 결제 전 회원
    # m2 = 결제 후 회원
    # t1 = 마스터 트레이너 (공지, 게시물 수정, 삭제, 회원 가입 신청 승인 등 가 다능)
    # t2 = 트레이너 (상위 조건 다름)

    center = models.CharField(max_length=30, null=True, blank=True)

    # 회원은 가입한 센터명
    # 트레이너는 소속 센터명

    reservationAvailable = models.BooleanField() #결제 조건에 따라 예약 가능 상태

    reserving = models.CharField(max_length=10, null=True, blank=True) #예약한 수업 id

    def __str__(self):
        return self.userId


