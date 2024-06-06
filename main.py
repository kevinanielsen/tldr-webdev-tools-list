import imaplib, email
import json
from read_email import extract_section_and_links, get_body, get_data_to_search, get_emails, search

def write_to_output(msgs):
  outputs = []
  for i, msg_data in enumerate(msgs[::-1]):
    for response_part in msg_data:
      if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])
        # Get the email body
        body = get_body(msg)
        # Handling errors related to unicodenecode
        try:
          data_to_search = get_data_to_search(body)
          if (len(data_to_search) > 1):
            section_text, links = extract_section_and_links(data_to_search)
            if section_text and links:
              with open('output/raw_output.json', 'w') as f:
                json.dump(section_text, f, indent=2)


              sections = section_text.split("\r\n\r\n")
              for i, section in enumerate(sections):
                if section.find("\r\n") == -1 and section.find("(") != -1 and section.find(")") != -1:
                  title = section.strip().split("(")[0].strip()
                  type = section.split("(")[1].split(")")[0].strip()
                  description = sections[i+1].replace("\r\n", " ").strip()
                  url_lookup = section.split("[")[1].split("]")[0].strip()

                  url = ""

                  for link in links:
                    if link[0] == url_lookup:
                      url = link[1]

                  outputs.append({
                    "type": type,
                    "title": title,
                    "description": description,
                    "url": url
                  })

            else:
              print("Section or links not found.")

        except UnicodeEncodeError as e:
            pass
  return outputs

def main():
  user = 'keveran@gmail.com'
  password = 'cfsb kxre absh hawf'
  imap_url = 'imap.gmail.com'

  con = imaplib.IMAP4_SSL(imap_url)
  con.login(user, password)
  con.select('TLDR')

  msgs = get_emails(search('FROM', '@tldrnewsletter.com', con), con)

  outputs = write_to_output(msgs)
  with open('output/output.json', 'w') as f:
    json.dump(outputs, f, indent=2)

if __name__ == '__main__':
    main()
