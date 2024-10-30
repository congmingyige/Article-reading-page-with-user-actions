<template>
    <div>

    </div>
</template>

<script>
  export default {
      name: 'Test',
        xyz: 'xyz',
      data(){
          this.work1();
          return {
              abc: 'abc'
          }
      },
      methods: {
          work1: function() {
            this.$http({
                    method: 'POST',
                    url: "http://127.0.0.1:8005/test",
                    headers: {
                      'sessionKey': this.sessionKey
                  }
                }).then((response) => {
                    //console.log(response.headers['X-CSRF-TOKEN']);
                    //console.log(document.cookie);
                    console.log(response.headers.get('username'));
                    console.log(response.headers);
                    console.log(response);
                    console.log(response['username']);
                },
                (response) => {
                  alert('数据传输失败');
                });
          }
      }
  }
</script>
