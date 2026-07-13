from typing import Dict, Any


class MarketCollector:

    @staticmethod
    def collect(controller) -> Dict[str, Dict[str, Any]]:

        ranking_rows: Dict[str, Dict[str, Any]] = {}

        for market in controller.MARKETS:

            controller._merge_rank_rows(
                ranking_rows,
                controller._request_amount_rank(market),
                "amountRank",
                market,
            )

            controller.pause(controller.TR_DELAY_MS)

        return ranking_rows