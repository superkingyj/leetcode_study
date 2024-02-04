import java.util.HashSet;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;

class FileInfo {
    String fileName;
    String fileVolume;
    public FileInfo(String fileName, String fileVolume){
        this.fileName = fileName;
        this.fileVolume = fileVolume;
    }
}

class Solution {
    public static final int MAX_FOLDER_NUM = 2000;
    public static final int MAX_FILE_NUM = 1000;
    public static HashSet<String> exceptions = new HashSet<String>();
    public static HashSet<String> selections = new HashSet<String>();
    public static HashMap<String, Object> graph = new HashMap<>();
    public static HashMap<String, Object> fileInfo = new HashMap<>();
    public static Queue<String> q = new LinkedList<>();
    public static int totalVolume;
    public static int totalCount;

    public int getVolume(String string){
        String number = "";
        int volume = 0;
        for(int i=0; i<string.length(); i++){
            try{
                Integer.parseInt(Character.toString(string.charAt(i)));
                number += Character.toString(string.charAt(i));
            }
            catch(NumberFormatException ex){
                if(string.charAt(i) == 'K'){
                    volume = Integer.parseInt(number) * 1024;
                }
                else{
                    volume = Integer.parseInt(number);
                }
                break;
            }
        }
        return volume;
    }

    public void BFS(){
        q.add("root");
        System.out.println(q);

        while(!q.isEmpty()){
            String folder = q.poll();
            System.out.println(folder);

            ArrayList files = (ArrayList)fileInfo.get(folder);
            System.out.println(files);

            if(files != null){
                for(int i=0; i<files.size(); i++){
                    FileInfo f = (FileInfo)files.get(i);
                    if(!exceptions.contains(f.fileName)){
                        totalCount++;
                        totalVolume += getVolume(f.fileVolume);
                    }
                }
            }

            ArrayList nextFolders = (ArrayList)graph.get(folder);
            if(nextFolders != null){
                for(int i=0; i<nextFolders.size(); i++){
                    // 검사할 폴더라면
                    if(selections.contains(nextFolders.get(i))){
                        q.add((String)nextFolders.get(i));
                    }
                }
            }

        }

    }

    public int[] solution(String[][] folders, String[][] files, String[] selected, String[] excepted) {
        int[] answer = {};
        int n = folders.length;
        int m = files.length;

        // 그래프 생성
        for(int i=0; i<n; i++){
            String highFolder = folders[i][1];
            String lowFolder = folders[i][0];
            if (!graph.containsKey(highFolder)){
                graph.put(highFolder, new ArrayList<>(){{
                    add(lowFolder);
                }});
            }
            else{
                ArrayList tmp = (ArrayList)graph.get(highFolder);
                tmp.add(lowFolder);
            }
        }
        System.out.println(graph);

        // 폴더별 파일 정보 저장
        for(int i=0; i<m; i++){
            String fileName = files[i][0];
            String fileVolume = files[i][1];
            String folderName = files[i][2];
            // 폴더명이 없다면
            if(!fileInfo.containsKey(folderName)){
                fileInfo.put(folderName, new ArrayList<FileInfo>(){{
                    add(new FileInfo(folderName, fileVolume));
                }});
            }
            else{
                ArrayList tmp = (ArrayList)fileInfo.get(folderName);
                tmp.add(new FileInfo(folderName, fileVolume));
            }
        }

        for(int i=0; i < selected.length; i++){
            selections.add(selected[i]);
        }

        for(int i=0; i< excepted.length; i++){
            exceptions.add(excepted[i]);
        }

        BFS();
        System.out.println(fileInfo);
        return new int[]{totalVolume, totalCount};
    }
}
