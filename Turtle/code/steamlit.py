#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 22:09:22 2023

@author: shubhamjuneja
"""

import streamlit as st
import numpy as np

ent_num = st.number_input('Enter the number for which you want to make the table',
                          min_value=(1),
                          max_value=(1000000000000))

if st.button('Create Table'):
    for i in range(1,11):
        st.write(str(ent_num)+'x'+str(i)+'='+str(ent_num*i))