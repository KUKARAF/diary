command! -nargs=* Diary call s:Diary(<q-args>)

function! s:Diary(args) abort
  let l:cmd = 'diary'
  if !empty(a:args)
    let l:cmd .= ' ' . a:args
  endif
  let l:files = systemlist(l:cmd)
  if v:shell_error
    echoerr 'diary failed: ' . join(l:files, "\n")
    return
  endif
  for l:f in l:files
    execute 'edit' fnameescape(l:f)
  endfor
endfunction
