 # Linux Daily admin commands</h2>
<!-- date: 2015-09-15 00:00:00 -->
<!-- category: linux -->
<!-- tags: linux, postfix, mailx, mailq, postqueue -->
Postfix:

    mailq                 # show queue
    postqueue -f          # Resend all queued messages
    postsuper -d ALL      # clear message queue
    postcat -q            # Show message (-v)

selinux immediately change:

    getenforce            # show selinux state
    setenforce 0          # turn off selinux