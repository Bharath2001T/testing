def merge_mails(mail1, mail2):
  """Merges two mails into a single mail."""
  merged_mail = mail1.copy()
  merged_mail.update(mail2)
  return merged_mail

if __name__ == "__main__":
  mail1 = {
      "from": "johndoe@example.com",
      "to": "janedoe@example.com",
      "subject": "Hello",
      "body": "This is the first mail.",
  }
  mail2 = {
      "from": "janedoe@example.com",
      "to": "johndoe@example.com",
      "subject": "Hi",
      "body": "This is the second mail.",
  }
  merged_mail = merge_mails(mail1, mail2)
  print(merged_mail)

  output::

  {'from': 'janedoe@example.com', 'to': 'johndoe@example.com', 'subject': 'Hi', 'body': 'This is the second mail.'}
