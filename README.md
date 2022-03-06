# LATIHAN4DPBO2022

## Saya Muhamad Firmansyah 2010021 mengerjakan Latihan 4 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

Sebuah repository untuk mengunggah kodingan dari latihan dpbo 2022

![DESIGN](https://user-images.githubusercontent.com/99308745/156923546-8d8deea9-0c3d-43ad-a620-480dd43c811d.png)

- Semua class yang sudah dispesifikasikan di soal saya masukan kedalam file yang terpisah, terdapat file Vehicle, Ship, Airplane, Person, Job, Driver dan Main/Index
- Semua class selain main/index memiliki metode get, set, konstruktor, semua ini dibutuhkan untuk memanggil semua variabel yang di buat
- Terdapat 2 implementasi pada program ini yang pertama Multiple Inheritance dan dan yang kedua Hierarchical Inheritance
- Implementasi pertama  mempunyai class Person, Job, Driver dimana Driver memiliki parent yaitu person dan juga job, mengapa? karena driver pasti memiliki hubungan seperti nama, jk, dan nim yang ada di class person, lalu driver juga memiliki hubungan seperti NIP, companyname, dan posisi pada company tersebut yang ada di class job. case ini merupakan implementasi Multiple Inheritance karena class driver mempunyai 2 parent yaitu person dan job.
- Implementasi kedua mempunyai class Vehicle, Ship, Airplane dimana Vehicle merupakan parent dari ship dan juga airplane, mengapa? karena class ship pasti memiliki hubungan seperti nama, fuelType, maxPassengers yang ada di class vehicle, lalu class airplane juga pasti memiliki hubungan seperti nama, fuelType, maxPassengers yang ada di class vehicle. case ini merupakan implementasi Hierarchical Inheritance karena class ship dan juga airplane mempunyai parent yang sama yaitu vehicle.
