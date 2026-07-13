from collections import defaultdict
from typing import Any, Dict, List


class SectorBuilder:

    def build(self, stocks: Dict[str, Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:

        sectors = defaultdict(list)

        for stock in stocks.values():

            sector = stock.get("sector") or "기타"

            sectors[sector].append(stock)

        for sector in sectors:

            sectors[sector].sort(
                key=lambda x: (
                    int(x.get("tradeAmountMillion") or 0),
                    int(x.get("volume") or 0),
                ),
                reverse=True,
            )

        return dict(sectors)