from utxo_manager import UTXOManager
from mempool import Mempool
from block import mine_block
from tests.test_scenarios import run_tests

def main():
    utxo_manager = UTXOManager()
    mempool = Mempool()

    genesis = [
        ("Alice", 50.0),
        ("Bob", 30.0),
        ("Charlie", 20.0),
        ("David", 10.0),
        ("Eve", 5.0),
    ]

    for i, (owner, amt) in enumerate(genesis):
        utxo_manager.add_utxo("genesis", i, amt, owner)

    while True:
        print("\n=== Bitcoin Transaction Simulator ===")
        print("Initial UTXOs (Genesis Block):")
        for owner, amt in genesis:
            print(f"- {owner} : {amt} BTC")

        print("\nMain Menu:")
        print("1. Create new transaction")
        print("2. View UTXO set")
        print("3. View mempool")
        print("4. Mine block")
        print("5. Run test scenarios")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "6":
            break
if __name__ == "__main__":
    main()

