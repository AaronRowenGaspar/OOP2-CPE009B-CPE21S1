class Accounts():
  def __init__(self, account_number, account_firstname, account_lastname, current_balance, address, email):
    self.account_number = account_number
    self.account_firstname = account_firstname
    self.account_lastname = account_lastname
    self.current_balance = Current_balance
    self.address = address
    self.email = email

  def update_address(new_address):
    Accounts.address = new_address

  def update_email(new_email):
    Accounts.email = new_email