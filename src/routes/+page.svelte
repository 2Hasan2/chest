<script>
  import { onMount } from "svelte";

  let messages;

  let send=(e)=>{
     e.preventDefault();

        const formData = new FormData();
        formData.append('file', file.files[0]);

        fetch('http://127.0.0.1:1010/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.warn(error)
            });
  }

</script>

<h2 class="text-cenetr">CT Scan Lung Disease Prediction</h2>
<h4 class="text-cenetr">Upload an image and click submit</h4>
<form
  class="p-3 text-center"
  method="post"
  action="/"
  enctype="multipart/form-data"
>
  <p>
    <input type="file" name="file" id="file" class="inputfile" />
    <label for="file">Choose a file</label>
  </p>
  <p>
    <input on:click={send} class="submitbutton" type="submit" name="submit" value="Submit" />
  </p>
</form>

{#if messages}
  <p style="color:black;">
    Diagnosis for the following image is: <u
      ><h3 style="color:black;">{messages[0]}</h3></u
    ><br />
  </p>
  <img src={messages[1]} width="300" , height="225" />
{/if}

<style>
  @import "./+page.css";
</style>
