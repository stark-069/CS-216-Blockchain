def mine_block(miner, mempool, utxo_manager, num_txs=5):
    selected = mempool.get_top_transactions(num_txs)
    total_fees = 0.0

    print(f"Selected {len(selected)} transactions from mempool.")

    for entry in selected:
        tx = entry["tx"]
        fee = entry["fee"]
        total_fees += fee

        for inp in tx["inputs"]:
            utxo_manager.remove_utxo(inp["prev_tx"], inp["index"])

        for i, out in enumerate(tx["outputs"]):
            utxo_manager.add_utxo(tx["tx_id"], i, out["amount"], out["address"])

        mempool.remove_transaction(tx["tx_id"])

    utxo_manager.add_utxo("coinbase", 0, total_fees, miner)
    print(f"Miner {miner} receives {total_fees} BTC")
    print("Block mined successfully!")
