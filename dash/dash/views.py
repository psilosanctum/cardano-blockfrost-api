from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html',)


class BarData(APIView):
    def get(self, request):
        path = 'converted_data/gross_income_by_wallet_2021.csv'

        df = pd.read_csv(path, index_col=[0])
        df["amount_usd"] = df["amount_usd"].round(decimals=2)

        wallets = list(df.wallets)
        amount_ada = list(df.amount_ada)
        amount_usd = list(df.amount_usd)

        data = {
            'wallets': wallets,
            'ada': amount_ada,
            'usd': amount_usd,
        }
        return Response(data)


class TransactionsOverTime(APIView):
    def get(self, request):
        path = 'epoch_data/converted_epoch_data.csv'

        df = pd.read_csv(path, index_col=[0])

        epoch = list(df.epoch)
        transactions = list(df.tx_count)
        fees = list(df.fees)
        avg_cost = list(df.avg_transaction_cost)

        data = {
            'epoch': epoch,
            'transactions': transactions,
            'fees': fees,
            'avg_cost': avg_cost

        }
        return Response(data)


class RewardsOverTimeData(APIView):
    def get(self, request):
        path = 'converted_data/rewards_converted_to_dollars.csv'

        df = pd.read_csv(path, index_col=[0])
        df["usd"] = df["usd"].round(decimals=2)

        epoch = list(df.epoch)
        amount_ada = list(df.amount)
        amount_usd = list(df.usd)
        reward_date = list(df.reward_date)
        market_price = list(df.market_price)

        data = {
            'epoch': epoch,
            'ada': amount_ada,
            'usd': amount_usd,
            'reward_date': reward_date,
            'market_price': market_price,
        }
        return Response(data)
