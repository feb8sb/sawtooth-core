# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
  
import pytest
import logging
import json
import aiohttp
import asyncio
import hashlib
import cbor
import base64
import urllib

from sawtooth_validation.rest_client import RestClient

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

                                      
from sawtooth_validation.base import DepTxnBaseTest

from fixtures import setup_write_check,\
                     setup_transact_savings,setup_send_payment,\
                     setup_invalid,setup_deposit_checking,\
                     setup_dep_accounts,setup_supply_agent,\
                     setup_dep_accounts,setup_supply_agent, setup_invalid_write_check,\
                     setup_amalgamate_accounts, setup_invalid_transact_savings, \
                     setup_transact_savings,setup_invalid_send_payment, setup_invalid_amalgamate_accounts, \
                     setup_invalid_deposit_checking


class TestSmallBankDependentTxns(DepTxnBaseTest):
    async def test_acc_dep_txns(self,setup_dep_accounts):  
        batch_list = setup_dep_accounts
                 
        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))
        print(response)
             
        self.assert_batch_validity(response)
        self.assert_txn_validity(response)

    
    async def test_deposit_checking_txns(self,setup_deposit_checking):  
        batch_list = setup_deposit_checking
                
        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))
            
        self.assert_batch_validity(response)
        self.assert_txn_validity(response)
    
    async def test_send_payment_txns(self,setup_send_payment):  
        batch_list = setup_send_payment
                
        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))
            
        self.assert_batch_validity(response)
        self.assert_txn_validity(response)
        
        
    async def test_write_check_txns(self,setup_write_check):  
        batch_list = setup_write_check

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response)

    async def test_invalid_write_check_txns(self,setup_invalid_write_check):  
        batch_list = setup_invalid_write_check

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response)

    async def test_setup_invalid_deposit_checking(self,setup_invalid_deposit_checking):  
        batch_list = setup_invalid_deposit_checking

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response)

    async def test_invalid_send_payment_txns(self,setup_invalid_send_payment):  
        batch_list = setup_invalid_send_payment

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response)

    async def test_transact_savings_txns(self,setup_transact_savings):  
        batch_list = setup_transact_savings

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response) 

    async def test_invalid_transact_savings_txns(self,setup_invalid_transact_savings):  
        batch_list = setup_invalid_transact_savings

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response)   


    async def test_amalgamate_accounts_txns(self,setup_amalgamate_accounts):  
        batch_list = setup_amalgamate_accounts

        for batch in batch_list:
            try:
                response = self.post_batch(batch)
            except urllib.error.HTTPError as error:
                response = json.loads(error.fp.read().decode('utf-8'))

        self.assert_batch_validity(response)
        self.assert_txn_validity(response) 
        
