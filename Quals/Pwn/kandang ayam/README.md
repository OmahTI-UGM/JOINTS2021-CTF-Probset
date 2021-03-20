# Desc

Who doesn't love chicken?

# Note untuk panitia

\-

# Flow singkat solver

Recon:

- Terdapat format string vulnerability
- Terdapat double free vulnerability

Soal heap standard (relatif lebih mudah). Leak libc dengan vuln format string, leak heap dengan vuln double free. Lalu atur heap agar mereturn address `__malloc_hook` saat kita melakukan `malloc`. Overwrite `__malloc_hook` dengan address `one_gadget`. Lakukan `malloc` agar mentrigger `one_gadget`.
