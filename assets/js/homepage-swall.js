// sweetalert

document.addEventListener('DOMContentLoaded', function() {
    Swal.fire({
      title: "<strong style='font-family: 'Raleway';'>Halooo Selamat Datang di Official Website Kami!</strong>",
      iconHtml: '<img src="assets/img/gif/hello-cute.gif" width="150" style="border: none; border-radius: 100%;">',
      html: `
        Jangan lupa untuk mengunjungi
        <a href="Sosial-Media.html" target='_blank'><b>Sosial Media</b></a>,
        kami iyaaaak!!
      `,
      showCloseButton: true,
      showCancelButton: false,
      focusConfirm: false,
      confirmButtonText: `
        <i class="fa fa-thumbs-up"></i> Siaap!
      `,
      confirmButtonAriaLabel: "Thumbs up, great!",
    });
    
  });