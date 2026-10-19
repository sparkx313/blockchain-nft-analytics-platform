import math
from typing import Dict, List
from collections import Counter

def calculate_rarity_score(traits: Dict[str, str], collection_traits: Dict[str, Counter]) -> float:
    score = 0
    for trait_type, trait_value in traits.items():
        if trait_type not in collection_traits:
            continue
        counter = collection_traits[trait_type]
        total = sum(counter.values())
        freq = counter.get(trait_value, 1) / total
        score += -math.log2(freq)
    return score

COLLECTION_TRAITS = {
    "Background": Counter({"Blue": 3000, "Red": 2000, "Gold": 500, "Holographic": 50}),
    "Eyes": Counter({"Normal": 4000, "Laser": 800, "Diamond": 100, "Void": 10}),
    "Mouth": Counter({"Smile": 3500, "Grin": 2000, "Frown": 1000, "Gold Tooth": 200}),
    "Hat": Counter({"None": 4000, "Cap": 2000, "Crown": 300, "Halo": 20}),
}

SAMPLE_NFTS = [
    {"id": 1, "traits": {"Background": "Blue", "Eyes": "Normal", "Mouth": "Smile", "Hat": "None"}},
    {"id": 2, "traits": {"Background": "Gold", "Eyes": "Laser", "Mouth": "Grin", "Hat": "Cap"}},
    {"id": 3, "traits": {"Background": "Holographic", "Eyes": "Diamond", "Mouth": "Gold Tooth", "Hat": "Crown"}},
    {"id": 4, "traits": {"Background": "Red", "Eyes": "Void", "Mouth": "Frown", "Hat": "Halo"}},
]

if __name__ == "__main__":
    scored = []
    for nft in SAMPLE_NFTS:
        score = calculate_rarity_score(nft["traits"], COLLECTION_TRAITS)
        scored.append((nft["id"], score, nft["traits"]))
    scored.sort(key=lambda x: x[1], reverse=True)
    print(f"{'Rank':<5} {'NFT ID':<8} {'Rarity Score':<14} Traits")
    print("-" * 70)
    for rank, (nft_id, score, traits) in enumerate(scored, 1):
        trait_str = ", ".join(f"{k}:{v}" for k, v in traits.items())
        print(f"{rank:<5} #{nft_id:<7} {score:<14.4f} {trait_str}")
