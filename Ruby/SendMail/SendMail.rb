#! /usr/bin/env ruby

# This script will read SMTP reladed information from a YAML file and then sent out a mail.
# The mail content is from outside.

if ARGV[0].nil? or ARGV[1].nil? or ARGV[2].nil?
    puts "Error::LackParameters"
    exit
else
    _para_sender    = ARGV[0]
    _para_subject   = ARGV[1]
    _para_mail_body = ARGV[2]
end

require 'json'
require 'time'
require 'net/smtp'
Net.instance_eval {remove_const :SMTPSession} if defined?(Net::SMTPSession)
require 'net/pop'
Net::POP.instance_eval {remove_const :Revision} if defined?(Net::POP::Revision)
Net.instance_eval {remove_const :POP} if defined?(Net::POP)
Net.instance_eval {remove_const :POPSession} if defined?(Net::POPSession)
Net.instance_eval {remove_const :POP3Session} if defined?(Net::POP3Session)
Net.instance_eval {remove_const :APOPSession} if defined?(Net::APOPSession)
require 'tlsmail'

# Fetch configuration items
_json_File_Name  = __FILE__ + ".json"
_json_File_Parse = JSON.parse(File.read(_json_File_Name))
## For each
_smtp_server        = _json_File_Parse["configuration"][_para_sender]["smtp_server"]
_smtp_port          = _json_File_Parse["configuration"][_para_sender]["smtp_port"]
_smtp_domain        = _json_File_Parse["configuration"][_para_sender]["smtp_domain"]
_smtp_username      = _json_File_Parse["configuration"][_para_sender]["smtp_username"]
_smtp_password      = _json_File_Parse["configuration"][_para_sender]["smtp_password"]
_smtp_mail_from     = _json_File_Parse["configuration"][_para_sender]["smtp_mail_from"]
_smtp_mail_to_list  = _json_File_Parse["mail_to_list"].to_s.gsub("[","").gsub("]","")
_smtp_mail_pre      = _json_File_Parse["mail_content"]["mail_subject_prefix"]
_smtp_mail_sign     = _json_File_Parse["mail_content"]["mail_signature"]

# Mail Body
_message_body = <<MAILEOF
From: #{_smtp_mail_from}
To: #{_smtp_mail_to_list}
Date: #{Time.now.rfc2822}
Subject: #{_smtp_mail_pre} #{_para_subject}

#{_para_mail_body}

#{_smtp_mail_sign}
MAILEOF

# Start to Send
Net::SMTP.enable_tls(OpenSSL::SSL::VERIFY_NONE)
Net::SMTP.new(_smtp_server, _smtp_port).start(
                _smtp_domain,
                _smtp_username,
                _smtp_password,
                :login) do |smtp|
                            smtp.send_message(_message_body,
                                              _smtp_mail_from,
                                              _smtp_mail_to_list)
end
puts "Script[" + __FILE__ + "] :: End"

