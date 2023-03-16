{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a5bdb9b2-c6b6-4a0b-8f60-236f437b9098",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (1.20.0)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: semver in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.13.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (3.1.31)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.28.2)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (8.1.3)\n",
      "Requirement already satisfied: tornado>=6.0.3 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (6.2)\n",
      "Requirement already satisfied: numpy in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.24.2)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: toml in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: blinker>=1.0.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.5)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (13.3.2)\n",
      "Requirement already satisfied: pympler>=0.9 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: validators>=0.2 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: watchdog in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (2.3.1)\n",
      "Requirement already satisfied: altair<5,>=3.2.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (23.0)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (4.5.0)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (5.3.0)\n",
      "Requirement already satisfied: pandas<2,>=0.25 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: tzlocal>=1.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from streamlit) (4.2)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from altair<5,>=3.2.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from click>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from gitpython!=3.1.19->streamlit) (4.0.10)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from pandas<2,>=0.25->streamlit) (2022.7.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests>=2.4->streamlit) (3.0.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests>=2.4->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.14)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: tzdata in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from tzlocal>=1.1->streamlit) (2022.7)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (22.2.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\s-mat\\appdata\\local\\programs\\python\\python310\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f5897fee-16bd-435e-afb3-496bbfcd3c3e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4852f7c2-ff4b-4b07-b50d-32eed397b150",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('My first Streamlit app')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38df72c7-8797-4152-a1cd-6909c6ee0d24",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a7935e-1bd3-4537-a62f-94d890aed51f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2cccf3ba-0dfc-4f92-97ab-464272e7f193",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adbea347-45cd-4e90-9386-5559ffbd50c0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62d39dae-fd22-49d6-9f74-49ee96ea4f4e",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bcc9110-1ddf-4326-8ed2-0c157ec2f1c8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71bd6611-7e55-40c6-8e14-1c3d96fd5026",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
