class UserMailer < ApplicationMailer

  default from: "shinha97@gmail.com"

  # Subject can be set in your I18n file at config/locales/en.yml
  # with the following lookup:
  #
  #   en.user_mailer.contact_mail.subject
  #
  def contact_mail(user)
    @user = user
    @message =  user
    #from = user.item.user.email

    mail to: "shinha97@gmail.com", subject: "Immortals Website - New Mail"
  end
end
