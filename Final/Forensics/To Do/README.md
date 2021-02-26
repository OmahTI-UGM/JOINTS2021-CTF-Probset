## Judul Soal
To Do

## Deskripsi Soal

> I often forgot about my daily task. Since then, I created a To Do list webservice in order to list & manage my own TODO. <br><br> Unfortunately, It has a big flaws, so that I decided to discontinue this project.
---

## Hint
- Despite having a flaw, I managed to encrypt my data enough, so that it can only be decrypted if you have access to its original `source code`.
- If you're wondering about the `producer`, you can always check its `metadata`

---
## Proof of Concept

- From given pcap get a bunch of TLS & TCP-Socket packet, filter on TCP-socket got sslkeylogfile
- Decrypt TLS packet using sslkeylogfile, then got HTTP/2 packet
- From HTTP/2 packet, there're bunch of add/edit task requests. Furthermore, there're also SQLi attempt
- Everytime a new PDF was generated, there're an addition of Embedded object. Based on, attack payload we can conclude that there's LFI vulnerability based on WeasyPrint
- By mapping order of filename & its Embedded object, we recovered each of .bzr files
- After successfully retrieved the whole files, revert the .bzr repository to its latest commit
- From recovered repository, we got a set of Docker configuration + an encrypted directory `web`
- If we look up further, we can see `EncFS` command that took a part in `/app` decryption
- From here, we have 2 options, either run a `docker container` to get the `decrypted file` or using `PASSWD` to decrypt `EncFS` manually on a local host
- There's a AES helper which adds Encryption and Decryption support to the `Task description`
- From there just look up into `group_concat(description) whered id=1` query to obtain all of encrypted `admin notes`. Then, decrypt using `helper function`

## Solver

TBA

<br>

## Flag
JOINTS21{4lways_b3w4re_of_exp0s3d_vcs_even_it5_canonical_0ne} 

