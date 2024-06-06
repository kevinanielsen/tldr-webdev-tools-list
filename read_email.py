import re

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data

def get_emails(result_bytes, con):
    msgs = []  # all the email data are pushed inside an array
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

def get_data_to_search(body):
  data = body.decode('utf-8')
  indexstart = data.find("LAUNCHES & TOOLS")+ len("LAUNCHES & TOOLS")
  data2 = data[indexstart + 5: len(data)]

  data_to_search = data[indexstart:data.find("</div>")]
  return data_to_search

def extract_section_and_links(email_content):
    section_text = email_content[0: email_content.find("🎁")].strip()

    # Extract link numbers mentioned in the section text
    link_numbers_pattern = re.compile(r'\[(\d+)\]')
    mentioned_links = link_numbers_pattern.findall(section_text)

    # Extract all links from the email content
    link_pattern = re.compile(r'\[(\d+)\] (https?://[^\s]+)')
    all_links = link_pattern.findall(email_content)

    # Filter only the mentioned links
    filtered_links = [link for link in all_links if link[0] in mentioned_links]

    return section_text, filtered_links
