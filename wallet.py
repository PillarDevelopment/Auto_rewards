import settings
from noahsdk.sdk.wallet import NoahWallet

wallet_from = NoahWallet.create(mnemonic=settings.MNEMONIC)
